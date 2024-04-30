json.device do
    json.identifier(@device["name"].split("/").last())

    json.policy do
        json.name(@device["policyName"].split("/").last())
    end
 
    json.appliedPolicy do
        json.name(@device["appliedPolicyName"].split("/").last())
        json.syncTime(Time.parse(@device["lastPolicySyncTime"]).to_i())
    end
end
