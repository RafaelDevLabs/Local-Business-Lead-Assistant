import type { LeadCreatePayload, LeadRead } from "@/types/lead";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function createLead(payload: LeadCreatePayload): Promise<LeadRead> {
  const response = await fetch(`${API_BASE_URL}/api/leads`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Unable to submit your request. Please try again.");
  }

  return response.json() as Promise<LeadRead>;
}
