Railsapp::Application.config.session_store(:active_record_store, key: "session_id", expire_after: 1.week)
