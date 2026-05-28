import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Local Growth Studio",
  description: "Simple websites and fast lead follow-up for local businesses.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
