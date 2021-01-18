import axios from '@/axios'

// Fazer login
const login = async variables => {
  const response = await axios.post(`login/`, variables)
  console.log('POST /login', response)
  return response
}

// Fazer signup
const signup = async variables => {
  const response = await axios.post(`register/`, variables)
  console.log('POST /singup', response)
  return response
}

export default {
  login,
  signup

}
