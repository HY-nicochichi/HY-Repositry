export default function() {

  const getAPIHostName: (client: any) => string
  = (client) => {
    if (client === 'webview') {
      return '10.0.2.2'
    }
    else {
      return 'localhost'
    }
  }

  const addQuery: (client: any) => string
  = (client) => {
    if (client === 'webview') {
      return '?client=webview'
    }
    else {
      return ''
    }
  }

  const pushRouter: (client: any, path: string) => any
  = (client, path) => {
    if (client === 'webview') {
      return {path: path, query: {client: 'webview'}}
    }
    else {
      return {path: path}
    }
  }

  return {
    getAPIHostName, addQuery, pushRouter
  }

}
