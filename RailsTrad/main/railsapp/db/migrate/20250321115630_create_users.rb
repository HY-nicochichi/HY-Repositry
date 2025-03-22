class CreateUsers < ActiveRecord::Migration[7.1]
  def change
    create_table :users do |t|
      t.string :mail
      t.string :name
      t.string :password_enc

      t.timestamps
    end
  end
end
