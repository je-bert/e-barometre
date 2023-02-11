/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,ts}"],
  theme: {
    extend: {
      colors: {
        primary: "#50b8ff",
      },
    },
  },
  plugins: [],
  prefix: "tw-",
  important: true,
};
