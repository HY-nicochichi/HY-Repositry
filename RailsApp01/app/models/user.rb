class User < ApplicationRecord
    validates :name, presence: true
    validates :email, presence: true
    validates :pass, presence: true
end
