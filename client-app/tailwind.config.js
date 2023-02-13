/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    colors: {
      primary: "#50b8ff",
      'custom-pale-gray': '#aadbfc26'
    },
    extend: {},
  },
  plugins: [],
  prefix: "tw-",
  important: true,
}
