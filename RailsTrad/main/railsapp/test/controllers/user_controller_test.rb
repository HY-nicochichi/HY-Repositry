require "test_helper"

class UserControllerTest < ActionController::TestCase

  test "user_show" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    get(:show)
    assert_redirected_to(session_new_path)
    get(:show, session: {user_id: user.id})
    assert_template("user/show")
  end

  test "user_new" do
    get(:new)
    assert_template("user/new")
  end

  test "user_edit" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    get(:edit)
    assert_redirected_to(session_new_path)
    get(
      :edit, 
      session: {user_id: user.id},
      params: {param: ""}
    )
    assert_redirected_to(user_edit_path(param: "ユーザーネーム"))
    get(
      :edit, 
      session: {user_id: user.id}, 
      params: {param: "ユーザーネーム"}
    )
    assert_template("user/edit")
  end

  test "user_create" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    post(:create, params: {mail: "foo", password: "foo", name: "foo"})
    assert_redirected_to(user_new_path)
    post(:create, params: {mail: "bar", password: "bar", name: "bar"})
    assert_redirected_to(root_path)
  end

  test "user_update" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    put(:update)
    assert_redirected_to(session_new_path)
    put(
      :update,
      session: {user_id: user.id},
      params: {param: "ユーザーネーム", current_val: "", new_val: "", check_val: ""}
    )
    assert_redirected_to(user_edit_path(param: "ユーザーネーム"))
    put(
      :update,
      session: {user_id: user.id}, 
      params: {param: "ユーザーネーム", current_val: "foo", new_val: "bar", check_val: "bar"}
    )
    assert_redirected_to(user_show_path)
  end

  test "user_destroy" do
    user = User.create(
      mail: "foo",
      password_enc: User.enc_val("foo"),
      name: "foo"
    )
    delete(:destroy)
    assert_redirected_to(session_new_path)
    delete(:destroy, session: {user_id: user.id})
    assert_redirected_to(root_path)
  end

end
