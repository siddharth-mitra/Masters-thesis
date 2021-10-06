# Master's Thesis
With the advances in Machine Learning, the deployment of Deep Learning models requiring GPUs at inference time is becoming increasingly common. GPUs are expensive resources that are often present in limited numbers as project resources. In a Kubernetes environment, where the inference services run in a serverless platform, autoscaling GPUs during inference time is a challenge. Companies often need to make informed decisions on the autoscaling approach to use while designing and implementing an inference serving system in such platforms.
 When selecting an appropriate autoscaling approach, there is often a requirement to trade-off between optimizing GPU utilization and having lower inference latency. One approach to improve GPU utilization is to scale based on GPU-based utilization metrics. However, these are not easily available on all Kubernetes platforms, and configuring them with the inbuilt Kubernetes resource, Horizontal Pod Autoscalers is non-trivial. GPU utilization-based autoscaling is not served out of the box in Kubernetes platforms, unlike its CPU autoscaling counterpart which boasts of a more mature system ecosystem of off-the-shelf autoscaling controls. One approach for autoscaling GPUs, provided as an off-the-shelf solution, uses the number of inflight requests to make a scaling decision (requests which are being served and not yet responded to).  
 In this thesis, we design and implement a simple autoscaling system that scales the GPUs based on the average GPU memory utilization. We compare both these approaches by studying their behavior in response to different environmental conditions that incrementally simulate real-world characteristics. These simulations model systems that are pounded by inference requests at a constant rate and another in which the systems are loaded with variable traffic. Through experiments, we show that the request-based autoscaling approach is better suited for use cases where the focus is on providing lower inference latency rather than better GPU utilization. In contrast, the GPU utilization-based autoscaling approach provides a more conservative way to utilize GPUs, generally leaving GPUs available for other use but at the cost of providing slow inference response times. 


















