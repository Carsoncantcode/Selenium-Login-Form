const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      width: {
        '200': '200px',
        '500': '500px',
        '800': '800px'
      },
      height: {
        '200': '200px',
        '500': '500px',
        '400': '400px'
      },
      colors: {
        customPurple: '#8f5cff',
        customPurpleBackground: 'CEB8FF',
        600: '#7a51cc', // a darker shade for hover
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    
  ],
}

