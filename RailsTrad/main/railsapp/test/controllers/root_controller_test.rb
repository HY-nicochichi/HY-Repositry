require "test_helper"

class RootControllerTest < ActionController::TestCase

  test "root_index" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    get(:index)
    assert_template("root/index")
    assert_match("ログイン", response.body)
    get(:index, session: {user_id: user.id})
    assert_template("root/index")
    assert_match("ログアウト", response.body)
  end

end
