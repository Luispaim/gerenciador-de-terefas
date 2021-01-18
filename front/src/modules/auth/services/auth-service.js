import axios, { onLogin } from '@/axios'

// Fazer login
const login = async variables => {
  const response = await axios.post(`token/`, variables)
  console.log('POST /login', response)
  const token = response.data
  await onLogin(token.access)
  return response
}

// Fazer signup
const signup = async variables => {
  const register = await axios.post(`register/`, variables)
  console.log('POST /singup', register)
  try {
    const response = await axios.post(`token/`, variables)
    const token = response.data
    await onLogin(token.access)
    return response
  } catch (error) {
    // console.log('Erro ao tentar fazer login: ', error)
    return error
  }
}

export default {
  login,
  signup

}
