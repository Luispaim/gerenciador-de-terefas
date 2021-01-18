import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'
import colors from 'vuetify/lib/util/colors'
import pt from 'vuetify/lib/locale/pt'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.use(Vuetify)

export default new Vuetify({
  lang: {
    locales: { pt },
    current: 'pt'
  },
  icons: {
    iconfont: 'md'
  },
  theme: {
    dark: false,
    themes: {
      light: {
        primary: colors.teal.darken4,
        secondary: colors.teal.darken3,
        accent: colors.teal.darken2,
        info: colors.cyan.darken3,
        error: colors.pink.darken1,
        success: colors.teal.darken1,
        warning: colors.red.darken4
      },
      dark: {
        primary: colors.grey.darken3,
        secondary: colors.grey.darken4,
        accent: colors.yellow.accent2,
        info: colors.blueGrey.darken2,
        error: colors.deepOrange.darken4,
        success: colors.teal.darken3,
        warning: colors.lime.darken1
      }
    }
  }
})
