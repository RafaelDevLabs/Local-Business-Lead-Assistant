"use client";

import { FormEvent, useState } from "react";
import { createLead } from "@/lib/api";
import type { LeadCreatePayload } from "@/types/lead";

type FormState = {
  name: string;
  phone: string;
  email: string;
  service_interest: string;
  preferred_date: string;
  message: string;
};

const initialForm: FormState = {
  name: "",
  phone: "",
  email: "",
  service_interest: "",
  preferred_date: "",
  message: "",
};

export function LeadForm() {
  const [form, setForm] = useState<FormState>(initialForm);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  function updateField(field: keyof FormState, value: string) {
    setForm((current) => ({ ...current, [field]: value }));
    setError(null);
    setSuccess(false);
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!form.name.trim() || !form.phone.trim()) {
      setError("Please enter your name and phone number.");
      return;
    }

    const payload: LeadCreatePayload = {
      name: form.name.trim(),
      phone: form.phone.trim(),
      email: cleanOptional(form.email),
      service_interest: cleanOptional(form.service_interest),
      preferred_date: form.preferred_date
        ? new Date(form.preferred_date).toISOString()
        : null,
      message: cleanOptional(form.message),
    };

    setIsSubmitting(true);
    setError(null);
    setSuccess(false);

    try {
      await createLead(payload);
      setForm(initialForm);
      setSuccess(true);
    } catch (submitError) {
      setError(
        submitError instanceof Error
          ? submitError.message
          : "Unable to submit your request. Please try again.",
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5">
      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-sm font-medium text-ink">Name</span>
          <input
            value={form.name}
            onChange={(event) => updateField("name", event.target.value)}
            className="mt-2 w-full rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
            placeholder="Your name"
            required
          />
        </label>

        <label className="block">
          <span className="text-sm font-medium text-ink">Phone</span>
          <input
            value={form.phone}
            onChange={(event) => updateField("phone", event.target.value)}
            className="mt-2 w-full rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
            placeholder="+40 700 000 000"
            required
          />
        </label>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-sm font-medium text-ink">Email</span>
          <input
            type="email"
            value={form.email}
            onChange={(event) => updateField("email", event.target.value)}
            className="mt-2 w-full rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
            placeholder="you@example.com"
          />
        </label>

        <label className="block">
          <span className="text-sm font-medium text-ink">Preferred date</span>
          <input
            type="datetime-local"
            value={form.preferred_date}
            onChange={(event) =>
              updateField("preferred_date", event.target.value)
            }
            className="mt-2 w-full rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
          />
        </label>
      </div>

      <label className="block">
        <span className="text-sm font-medium text-ink">Service interest</span>
        <input
          value={form.service_interest}
          onChange={(event) =>
            updateField("service_interest", event.target.value)
          }
          className="mt-2 w-full rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
          placeholder="Website, ads, SEO, booking setup..."
        />
      </label>

      <label className="block">
        <span className="text-sm font-medium text-ink">Message</span>
        <textarea
          value={form.message}
          onChange={(event) => updateField("message", event.target.value)}
          className="mt-2 min-h-32 w-full resize-y rounded-md border border-moss/30 bg-white px-4 py-3 text-ink outline-none transition focus:border-leaf focus:ring-2 focus:ring-leaf/20"
          placeholder="Tell us what you want to improve."
        />
      </label>

      {error ? (
        <p className="rounded-md border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          {error}
        </p>
      ) : null}

      {success ? (
        <p className="rounded-md border border-leaf/25 bg-leaf/10 px-4 py-3 text-sm text-leaf">
          Thanks. Your request was received and we will follow up shortly.
        </p>
      ) : null}

      <button
        type="submit"
        disabled={isSubmitting}
        className="inline-flex min-h-12 w-full items-center justify-center rounded-md bg-leaf px-5 py-3 font-semibold text-white transition hover:bg-ink disabled:cursor-not-allowed disabled:bg-moss sm:w-auto"
      >
        {isSubmitting ? "Sending..." : "Request a consultation"}
      </button>
    </form>
  );
}

function cleanOptional(value: string): string | null {
  const cleanValue = value.trim();
  return cleanValue ? cleanValue : null;
}
