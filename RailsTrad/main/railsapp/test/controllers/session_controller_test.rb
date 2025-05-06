require "test_helper"

class SessionControllerTest < ActionController::TestCase

  test "session_new" do
    get(:new)
    assert_template("session/new")
  end

  test "session_create" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    post(:create, params: {mail: "", password: ""})
    assert_redirected_to(session_new_path)
    post(:create, params: {mail: "foo", password: "foo"})
    assert_redirected_to(root_path)
  end

  test "session_destroy" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    user_id = user.id
    delete(:destroy)
    assert_redirected_to(session_new_path)
    delete(:destroy, session: {user_id: user_id})
    assert_redirected_to(root_path)
    user.destroy()
    delete(:destroy, session: {user_id: user_id})
    assert_redirected_to(session_new_path)
  end

end
