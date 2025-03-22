class User < ApplicationRecord

  def User.enc_val(string)
    if ActiveModel::SecurePassword.min_cost()
      cost = BCrypt::Engine::MIN_COST
    else
      cost = BCrypt::Engine.cost()
    end    
    return BCrypt::Password.create(string, cost: cost)
  end

  def correct_password?(password) 
    return BCrypt::Password.new(password_enc).is_password?(password)
  end

end
