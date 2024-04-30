class MainController < ApplicationController

    # GET "/enterprises/:enterprise_name"
    def index()
    end
    
    # GET "/enterprises/:enterprise_name/call"
    def call_get()
    end
    
    # POST "/enterprises/:enterprise_name/call"
    def call_post()
    end
    
    # GET "/enterprises/:enterprise_name/applications"
    def app()
    end
    
    # GET "/enterprises/:enterprise_name/applications/:package_name"
    def app_packname()
    end
    
    # GET "/enterprises/:enterprise_name/policies/new"
    def pol_new()
    end
    
    # GET "/enterprises/:enterprise_name/policies/:identifier"
    def pol_get()
    end
    
    # GET "/enterprises/:enterprise_name/policies"
    def pol_post()
    end
    
    # GET "/enterprises/:enterprise_name/policies/:identifier/qr"
    def pol_qr()
    end
    
    # GET "/enterprises/:enterprise_name/devices/:identifier"
    def dev()
    end
    
    # GET "/enterprises/:enterprise_name/devices/:identifier/policy"
    def dev_pol_get()
    end
    
    # GET "/enterprises/:enterprise_name/devices/:identifier/policy"
    def dev_pol_post()
    end
    
end
