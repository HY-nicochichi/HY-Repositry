class AdminUser < ApplicationRecord
  validates :google_oauth2_uid, presence: true
  validates :enterprise_name, presence: true  
end
