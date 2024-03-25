class CreateArticles < ActiveRecord::Migration[7.0]
  def change
    create_table :articles do |t|
      t.string :title, limit: 255
      t.string :body, limit: 255
      t.string :user, limit: 255

      t.timestamps
    end
  end
end
