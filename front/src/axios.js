import axios from 'axios'
import config from './config/config'
import { camelizeKeys, decamelizeKeys } from 'humps'

// token
const AUTH_TOKEN = 'token-access'

// salvando o token no localstorage
const onLogin = async (token) => {
  if (typeof window.localStorage !== 'undefined' && token) {
    window.localStorage.setItem(AUTH_TOKEN, token)
  }
}

// removendo o token do localstorage
const onLogout = async apollo => {
  if (typeof window.localStorage !== 'undefined') {
    window.localStorage.removeItem(AUTH_TOKEN)
  }
}

const instance = axios.create({})

instance.defaults.baseURL = config.apiURL

instance.interceptors.request.use(config => {
  console.log('Interceptando requisição: ', config)

  config.data = {
    ...config.data,
    curso: 'Vue JS'
  }
  if (config.headers['Content-Type'] === 'multipart/form-data') { return config }
  if (config.params) {
    config.params = decamelizeKeys(config.params)
  }
  if (config.data) {
    config.data = decamelizeKeys(config.data)
  }

  config.headers.common['Authorization'] = `JWT ${window.localStorage.getItem(AUTH_TOKEN)}`

  return config
}, error => {
  console.log('Erro ao fazer requisição: ', error)
  return Promise.reject(error)
})

instance.interceptors.response.use(response => {
  console.log('Interceptando resposta...', response)
  if (Array.isArray(response.data)) {
    response.data = response.data.slice(1, 3)
  }
  if (
    response.data &&
    response.headers['content-type'] === 'application/json'
  ) {
    response.data = camelizeKeys(response.data)
  }
  return response
}, error => {
  console.log('Erro capturado no interceptador de respostas: ', error)
  return Promise.reject(error)
})

export default instance

export {
  AUTH_TOKEN,
  onLogin,
  onLogout
}
