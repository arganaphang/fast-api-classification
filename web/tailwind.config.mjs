/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        dark: "#131313",
        light: "#f3f3f3",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
