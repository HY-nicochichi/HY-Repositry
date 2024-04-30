class ApiController < ApplicationController

    # GET "/api/enterprises/:enterprise_name/devices/:identifier/policy"
    def get()
        api_authorization_required()
        name = "enterprises/#{params["enterprise_name"]}/devices/#{params["identifier"]}"
        @device = AndroidManagementApi.call("GET /#{name}")
        @policies = AndroidManagementApi.call("GET /enterprises/#{params["enterprise_name"]}/policies")["policies"]
        unless @policies
            @policies = []
        end
    end

    # PATCH "/api/enterprises/:enterprise_name/devices/:identifier/policy"
    def patch()
        api_authorization_required()
        policy_name = params["policy"]["name"]
        unless policy_name
            return render(plain: "policy.name is required", status: 400)
        end
        name = "enterprises/#{params["enterprise_name"]}/devices/#{params["identifier"]}"
        payload = {"policyName": policy_name}
        AndroidManagementApi.call("PATCH /#{name}?updateMask=policyName", payload: payload)
        @device = AndroidManagementApi.call("GET /#{name}")
    end

end
