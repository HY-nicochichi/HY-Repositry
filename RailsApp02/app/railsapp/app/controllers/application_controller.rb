class ApplicationController < ActionController::Base
    include UsersHelper
    include SessionsHelper
    add_flash_types("success", "info", "warning", "danger")
end
