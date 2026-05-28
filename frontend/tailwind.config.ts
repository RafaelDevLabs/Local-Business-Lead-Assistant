import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#17211b",
        moss: "#52715d",
        leaf: "#2f7d52",
        sun: "#f3b43f",
        cloud: "#f6f8f4",
      },
    },
  },
  plugins: [],
};

export default config;
