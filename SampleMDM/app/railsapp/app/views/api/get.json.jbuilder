json.device() do
    json.identifier(@device["name"].split("/").last())

    json.policy() do
        json.name(@device["policyName"].split("/").last())
    end
 
    json.appliedPolicy() do
        json.name(@device["appliedPolicyName"].split("/").last())
        json.syncTime(Time.parse(@device["lastPolicySyncTime"]).to_i())
    end

    if @policies.is_a?(Enumerable)
        json.availablePolicies(@policies) do |policy|
            json.name(policy["name"].split("/").last())
        end
    end
end

json.device do
    json.identifier @device["name"].split("/").last

    json.policy do
        json.name @device["policyName"].split("/").last
    end
 
    json.appliedPolicy do
        json.name @device["appliedPolicyName"].split("/").last
        json.syncTime Time.parse(@device["lastPolicySyncTime"]).to_i
    end

    if @policies.is_a? Enumerable
        json.availablePolicies(@policies) do |policy|
            json.name policy["name"].split("/").last
        end
    end
end
