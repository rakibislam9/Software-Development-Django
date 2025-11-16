/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //Templates at the project level
    "./**/templates/**/*.html", // Templates inside app level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

