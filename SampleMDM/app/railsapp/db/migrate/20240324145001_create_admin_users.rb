class CreateAdminUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :admin_users do |t|
      t.text :google_oauth2_uid
      t.text :enterprise_name

      t.timestamps
    end
  end
end
