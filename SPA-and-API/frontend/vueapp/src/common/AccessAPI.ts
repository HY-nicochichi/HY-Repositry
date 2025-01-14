import { Response } from './Interface'
import { getJWT } from './ManageJWT'

async function postJWTCreate(mail_address: string, password: string): Promise<Response> {
  const resp: Response = await fetch(
    'http://localhost:5000/api/jwt/create', {
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
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function postUserCreate(mail_address: string, password: string, user_name: string): Promise<Response> {
  const resp: Response = await fetch(
    'http://localhost:5000/api/user/create', {
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
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function getUserInfo(): Promise<Response> {
  const resp: Response = await fetch(
    'http://localhost:5000/api/user/info', {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Authorization': 'Bearer ' + getJWT()
      }
    }
  )
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function postUserUpdate(param: string, current_value: string, new_value: string, check_value: string): Promise<Response> {
  const resp: Response = await fetch(
    'http://localhost:5000/api/user/update', {
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
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function getUserDelete(): Promise<Response> {
  const resp: Response = await fetch(
    'http://localhost:5000/api/user/delete', {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Authorization': 'Bearer ' + getJWT()
      }
    }
  )
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

export {
  postJWTCreate, postUserCreate, getUserInfo, postUserUpdate, getUserDelete
}
