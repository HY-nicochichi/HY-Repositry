interface Resp {
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

export type {
  Resp, User, Alert
}
