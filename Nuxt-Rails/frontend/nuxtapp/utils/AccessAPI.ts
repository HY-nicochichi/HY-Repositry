import type { Response } from './Interface'
import { getJWT } from './ManageJWT'

const jwt_api_route = 'http://localhost:5000/jwt/'
const user_api_route = 'http://localhost:5000/user/'

async function accessJwtPost(mail: string, password: string): Promise<Response> {
  const resp: Response = await fetch(
    jwt_api_route, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        mail: mail, 
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

async function accessUserGet(): Promise<Response> {
  const resp: Response = await fetch(
    user_api_route, {
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

async function accessUserPost(mail: string, password: string, name: string): Promise<Response> {
  const resp: Response = await fetch(
    user_api_route, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        mail: mail, 
        password: password,
        name: name
      })
    }
  )
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function accessUserPut(param: string, current_val: string, new_val: string, check_val: string): Promise<Response> {
  const resp: Response = await fetch(
    user_api_route, {
      method: 'PUT',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + getJWT()
      },
      body: JSON.stringify({
        param: param,
        current_val: current_val, 
        new_val: new_val,
        check_val: check_val
      })
    }
  )
  const response: Response = {
    status: resp.status,
    json: await resp.json()
  }
  return response
}

async function accessUserDelete(): Promise<Response> {
  const resp: Response = await fetch(
    user_api_route, {
      method: 'DELETE',
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
  accessJwtPost, accessUserGet, accessUserPost, accessUserPut, accessUserDelete
}
