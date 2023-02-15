/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,ts}"],
  theme: {
    extend: {
      colors: {
        primary: "#50b8ff",
        "custom-pale-gray": "#aadbfc26",
      },
    },
  },
  plugins: [],
  prefix: "tw-",
  important: true,
};
