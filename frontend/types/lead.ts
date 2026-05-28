export type LeadCreatePayload = {
  name: string;
  phone: string;
  email?: string | null;
  service_interest?: string | null;
  preferred_date?: string | null;
  message?: string | null;
};

export type LeadRead = LeadCreatePayload & {
  id: string;
  status: "new" | "contacted" | "booked" | "lost";
  ai_summary: string | null;
  created_at: string;
  updated_at: string;
};
