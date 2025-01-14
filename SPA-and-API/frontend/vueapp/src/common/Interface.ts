interface Response {
  status: number
  json: any
}

interface User {
  login: boolean
  name: string
  mail: string
}
  
interface Alert {
  show: boolean
  msg: string
}

export {
  Response, User, Alert
}
