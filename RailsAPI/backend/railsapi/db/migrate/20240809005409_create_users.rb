class CreateUsers < ActiveRecord::Migration[7.1]
  def change
    create_table :users do |t|
      t.string :mail
      t.string :digestpass
      t.string :username

      t.timestamps
    end
  end
end
