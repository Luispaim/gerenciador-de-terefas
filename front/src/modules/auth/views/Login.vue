<template>
  <v-container fill-height>
    <v-row
      justify="center"
      align="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="8"
        lg="6"
        xl="6"
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="primary"
            dark
          >
            <v-toolbar-title>{{ texts.toolbar }}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-progress-circular
              v-show="isLoading"
              indeterminate
              color="white"
              width="2"
            ></v-progress-circular>
          </v-toolbar>

          <v-card-text>
            <v-form>
              <v-text-field
                v-if="!isLogin"
                prepend-icon="person"
                name="firstName"
                label="Nome"
                type="text"
                :error-messages="firstNameErrors"
                :success="!$v.user.firstName.$invalid"
                v-model.trim="$v.user.firstName.$model"
              ></v-text-field>
              <v-text-field
                prepend-icon="email"
                name="email"
                label="Email"
                type="email"
                :error-messages="emailErrors"
                :success="!$v.user.email.$invalid"
                v-model.trim="$v.user.email.$model"
              ></v-text-field>
              <v-text-field
                prepend-icon="lock"
                name="password"
                label="Senha"
                type="password"
                :error-messages="passwordErrors"
                :success="!$v.user.password.$invalid"
                v-model.trim="$v.user.password.$model"
              ></v-text-field>
              <v-text-field
                v-if="!isLogin"
                prepend-icon="lock"
                name="password2"
                label="Confimar Senha"
                type="password"
                :error-messages="password2Errors"
                :success="!$v.user.password2.$invalid"
                v-model.trim="$v.user.password2.$model"
              ></v-text-field>
            </v-form>

            <v-btn
              block
              depressed
              @click="isLogin = !isLogin"
            >
              {{ texts.button }}
            </v-btn>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="$v.$invalid"
              color="secondary"
              large
              @click="submit"
            >{{ texts.toolbar }}</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
          <v-snackbar
            v-model="showSnackbar"
            top
            color="secondary"
          >
            {{ error }}
            <v-btn
              color="grey"
              text
              icon
              @click="showSnackbar = false"
            >
              <v-icon>close</v-icon>
            </v-btn>
          </v-snackbar>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'
import AuthService from './../services/auth-service'

export default {
  name: 'Login',
  data: () => ({
    error: undefined,
    isLogin: true,
    isLoading: false,
    showSnackbar: false,
    user: {
      firstName: '',
      email: '',
      password: '',
      password2: ''
    }
  }),
  validations () {
    const validations = {
      user: {
        email: {
          required,
          email
        },
        password: {
          required,
          minLength: minLength(6)
        }
      }
    }

    if (this.isLogin) { return validations }

    return {
      user: {
        ...validations.user,
        firstName: {
          required,
          minLength: minLength(3)
        },
        password2: {
          required,
          sameAsPassword: sameAs('password')
        }
      }
    }
  },
  computed: {
    texts () {
      return this.isLogin
        ? { toolbar: 'Entrar', button: 'Criar conta' }
        : { toolbar: 'Criar conta', button: 'Já tenho uma conta' }
    },
    firstNameErrors () {
      const errors = []
      const firstName = this.$v.user.firstName
      if (!firstName.$dirty) { return errors }
      !firstName.required && errors.push('Nome é obrigatório!')
      !firstName.minLength && errors.push(`Insira pelo menos ${firstName.$params.minLength.min} caracteres!`)
      return errors
    },
    emailErrors () {
      const errors = []
      const email = this.$v.user.email
      if (!email.$dirty) { return errors }
      !email.required && errors.push('Email é obrigatório!')
      !email.email && errors.push('Insira um email válido!')
      return errors
    },
    passwordErrors () {
      const errors = []
      const password = this.$v.user.password
      if (!password.$dirty) { return errors }
      !password.required && errors.push('Senha é obrigatória!')
      !password.minLength && errors.push(`Insira pelo menos ${password.$params.minLength.min} caracteres!`)
      return errors
    },
    password2Errors () {
      const errors = []
      const password2 = this.$v.user.password2
      if (!password2.$dirty) { return errors }
      !password2.required && errors.push('Senha é obrigatória!')
      !password2.sameAsPassword && errors.push('Senhas diferentes!')
      return errors
    }
  },
  methods: {
    async submit () {
      this.isLoading = true
      // Teste para ver se o loadind está funcionando
      // await new Promise(resolve => setTimeout(resolve, 3000))
      try {
        const authData = this.isLogin
          ? await AuthService.login(this.user)
          : await AuthService.signup(this.user)
        // console.log('authData', authData)
        if (authData.status === 200) {
          this.$router.push(this.$route.query.redirect || '/dashboard')
        }
      } catch (error) {
        // console.log('Erro ao tentar fazer login: ', error)
        this.error = error
        this.showSnackbar = true
      } finally {
        // console.log('Sempre executado!')
        this.isLoading = false
      }
    }
  }
}
</script>
