require "application_system_test_case"

class RootsTest < ApplicationSystemTestCase
  setup do
    @root = roots(:one)
  end

  test "visiting the index" do
    visit roots_url
    assert_selector "h1", text: "Roots"
  end

  test "should create root" do
    visit roots_url
    click_on "New root"

    click_on "Create Root"

    assert_text "Root was successfully created"
    click_on "Back"
  end

  test "should update Root" do
    visit root_url(@root)
    click_on "Edit this root", match: :first

    click_on "Update Root"

    assert_text "Root was successfully updated"
    click_on "Back"
  end

  test "should destroy Root" do
    visit root_url(@root)
    click_on "Destroy this root", match: :first

    assert_text "Root was successfully destroyed"
  end
end
