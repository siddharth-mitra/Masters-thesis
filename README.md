# Master's Thesis
Deploying inference models in production come with a number of challenges:

* Handling multiple machine learning models in a consistent manner. 
* Updating running models with new models. 
* Scaling models appropriately with constraints. 
* Monitoring models in production.

In this project, we are focusing on heterogeneous model servers. i.e, multi-model servers with a non-uniform set of models being hosted.
The goal of this project is to research an important question which falls within the domain of autoscaling.

**Are autoscaling decisions based on GPU utilization metrics more efficient than making decisions based on the number of inflight requests?**  

**Smart scheduler so that models can be scheduled into a new server(container) co-located with other models based on current GPU memory usage**


















