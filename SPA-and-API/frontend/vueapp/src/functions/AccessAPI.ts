import ManageJWT from './ManageJWT'
import ManageQuery from './ManageQuery'

const { getJWT } = ManageJWT()
const { getAPIHostName } = ManageQuery()

export default function() {

  const postJWTCreate: (client: any, mail_address: string, password: string) => Promise<{status: number, json: any}> 
  = async(client, mail_address, password) => {
    const resp: Response = await fetch(
      'http://' + getAPIHostName(client) + ':5000/api/jwt/create', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mail_address: mail_address, 
          password: password
        })
      }
    )
    const response: {status: number, json: any} = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const postUserCreate: (client: any, mail_address: string, password: string, user_name: string) => Promise<{status: number, json: any}>
  = async(client, mail_address, password, user_name) => {
    const resp: Response = await fetch(
      'http://' + getAPIHostName(client) + ':5000/api/user/create', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mail_address: mail_address, 
          password: password,
          user_name: user_name
        })
      }
    )
    const response: {status: number, json: any} = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const getUserInfo: (client: any) => Promise<{status: number, json: any}>
  = async(client) => {
    const resp: Response = await fetch(
      'http://' + getAPIHostName(client) + ':5000/api/user/info', {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Authorization': 'Bearer ' + getJWT()
        }
      }
    )
    const response: {status: number, json: any} = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const postUserUpdate: (client: any, param: string, current_value: string, new_value: string, check_value: string) => Promise<{status: number, json: any}>
  = async(client, param, current_value, new_value, check_value) => {
    const resp: Response = await fetch(
      'http://' + getAPIHostName(client) + ':5000/api/user/update', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + getJWT()
        },
        body: JSON.stringify({
          param: param,
          current_value: current_value, 
          new_value: new_value,
          check_value: check_value
        })
      }
    )
    const response: {status: number, json: any} = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const getUserDelete: (client: any) => Promise<{status: number, json: any}>
  = async(client) => {
    const resp: Response = await fetch(
      'http://' + getAPIHostName(client) + ':5000/api/user/delete', {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Authorization': 'Bearer ' + getJWT()
        }
      }
    )
    const response: {status: number, json: any} = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  return {
    postJWTCreate, postUserCreate, getUserInfo, postUserUpdate, getUserDelete
  }

}
