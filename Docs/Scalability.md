## Scalability
Scalability is a non-functional property of a system that describes the ability to appropriately handle increasing (and decreasing) workloads without performance degradation.

Once a model is in production it needs to be scaled
to the appropriate level for the concurrency, latency and
throughput requirements. It also needs to be reactive to
scale up and scale down as the demand placed on it changes
over time. 

###Horizontal autoscaling
When scaling your systems horizontally, you generally add more servers to spread the load across multiple machines. 

#### What is a Horizontal Pod Autoscaler?
Scales the number of pods based on observed metrics. 
The Horizontal Pod Autoscaler is implemented as a Kubernetes API resource and a controller. The resource determines the behavior of the controller. The controller periodically adjusts the number of replicas in a replication controller or deployment to match the observed metrics such as average CPU utilisation, average memory utilisation or any other custom metric to the target specified by the user.

### GPU Autoscaling
Models requiring GPUs at inference time are becoming
more common. However, correctly autoscaling models
which utilize GPUs is a challenge. 

* GPU duty cycle metrics are only becoming easily available on some Kubernetes Cloud platforms and configuring Horizontal Pod Autoscalers (HPAs) for them is not easy
* You need to combine the CPU usage of the running server alongside its GPU usage which is not an easy task to reconcile for
creating an autoscaling decision.
* Fractional GPU cannot be allocated to a pod. 

http://berb.github.io/diploma-thesis/original/024_scalability.html