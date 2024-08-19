import ManageJWT from './ManageJWT'

const { getJWT } = ManageJWT()

export default function() {

  const postJWTCreate = async(mail, password) => {
    const resp = await fetch(
      'https://spa-and-api-backend-7pahdmpb6a-an.a.run.app/api/jwt/create', {
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
    const response = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const postUserCreate = async(mail, password, username) => {
    const resp = await fetch(
      'https://spa-and-api-backend-7pahdmpb6a-an.a.run.app/api/user/create', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mail: mail, 
          password: password,
          username: username
        })
      }
    )
    const response = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const getUserInfo = async() => {
    const resp = await fetch(
      'https://spa-and-api-backend-7pahdmpb6a-an.a.run.app/api/user/info', {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Authorization': 'Bearer ' + getJWT()
        }
      }
    )
    const response = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const postUserUpdate = async(param, current_value, new_value, check_value) => {
    const resp = await fetch(
      'https://spa-and-api-backend-7pahdmpb6a-an.a.run.app/api/user/update', {
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
    const response = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  const getUserDelete = async() => {
    const resp = await fetch(
      'https://spa-and-api-backend-7pahdmpb6a-an.a.run.app/api/user/delete', {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Authorization': 'Bearer ' + getJWT()
        }
      }
    )
    const response = {
      status: resp.status,
      json: await resp.json()
    }
    return response
  }

  return {
    postJWTCreate, postUserCreate, getUserInfo, postUserUpdate, getUserDelete
  }

}
