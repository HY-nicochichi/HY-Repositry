module ApplicationHelper

    require "base64"
    require "googleauth"
    require "json"
    require "relax2/base"
    require "stringio"

    def page_title(title="Sample MDM")
        return title
    end

    def login_required()
        unless session["user"]
            session["return_to"] = request.fullpath
            return redirect_to("/auth/google_oauth2")
        end
    end

    def api_authorization_required()
        unless request.env["HTTP_AUTHORIZATION"] == "Bearer #{ENV["OREORE_API_KEY"]}"
            return render(plain: "Access Forbidden", status: 403)
        end
    end

    class AndroidManagementApi < Relax2::Base

        module Internal

            ACCESS_TOKEN_CACHE = Relax2::FileCache.new("oreoremdm", "android_management_api_access_token")

            module_function

            def service_account_string()
                unless @service_account_string
                    @service_account_string = Base64.decode64(ENV["SERVICE_ACCOUNT_CREDENTIAL_JSON"])
                end
            end

            def fetch_access_token(service_account_string)
                client = Google::Auth::ServiceAccountCredentials.make_creds(
                    json_key_io: StringIO.new(service_account_string),
                    scope: ["https://www.googleapis.com/auth/androidmanagement"]
                )
                client.fetch_access_token!()
                return client.access_token()
            end

            def auth_with_google(request, perform_request)
                unless service_account_string()
                    raise "configure is required"
                end
                cached_access_token = ACCESS_TOKEN_CACHE.load()
                if cached_access_token
                    access_token = cached_access_token
                else  
                    access_token = fetch_access_token(service_account_string())
                end
                service_account_json = JSON.parse(service_account_string())
                for elem in request.query_parameters
                    elem[1].gsub!("{project_id}", service_account_json["project_id"])
                end
                request.headers.push(["Authorization", "Bearer #{access_token}"])
                response = perform_request.call(request)
                if response.status == 401
                    if cached_access_token
                        ACCESS_TOKEN_CACHE.clear()
                        cached_access_token = nil
                        access_token = fetch_access_token(service_account_string())
                        for elem in request.headers
                            if elem[0] == "Authorization"
                                request.headers.reject!(elem)
                            end
                        end
                        request.headers.push(["Authorization", "Bearer #{access_token}"])
                        response = perform_request.call(request)
                    end
                elsif response.status < 300
                    unless cached_access_token
                        ACCESS_TOKEN_CACHE.save(access_token)
                    end
                end
                return response
            end

        end

        def self.call(url_and_params, payload=nil)
            args = url_and_params.strip.split(" ")
            if payload
                request = Relax2::Request.from(args: args, body: payload.to_json())
            else
                request = Relax2::Request.from(args: args)
            end
            response = super(request)
            return JSON.parse(response.body)
        end
  
        base_url("https://androidmanagement.googleapis.com/v1")

        interceptor(Internal.method(:auth_with_google))
        interceptor(:json_request)

    end

end
