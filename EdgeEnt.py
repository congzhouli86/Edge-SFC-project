import math
import random

# define access point class
class AP_node:
    service_type = ''
    node_id = 0
    def __init__(self, node_id, service_type):
        self.node_id = node_id
        self.service_type = service_type        
    def self_report(self):
        print ("I am AP node %d, my serive type is %s. " % (self.node_id, self.service_type))



# define container class for VNF
class VNF_C:
    node_id = 0 # the belonging of this container
    Avail = 1 # the availabilty of this container
    AP_id = 0 # deployed by which access point
    SFC_id = 0 # deployed by which SFC
    VNF_type = 0 # the type of VNF 
    CPU_num = 1 # how many cpus consumed by this VNF
    P_delay = 0 # processing delay of traffic passing this VNF
    def __init__(self, node_id, Avail):
        self.node_id = node_id
        self.Avail = Avail
    def deploy(self, AP_id, SFC_id, VNF_type, CPU_num):
        self.AP_id = AP_id
        self.SFC_id = SFC_id
        self.VNF_type = VNF_type
        self.CPU_num = CPU_num
    def get_delay(self, traffic): 
        self.P_delay = traffic / (self.CPU_num * self.VNF_type)
        return self.P_delay      
    
# define computing node class
class C_node:
    container_num = 0    
    node_id = 0
    CPU_num = 0 # how many cpu cores owned by this node
    def __init__(self, node_id, container_num):
        self.node_id = node_id
        self.container_num = container_num
    def self_report(self):
        print ("I am container node %d, I can hold %d containers. " % (self.node_id, self.container_num))
    def state_report(self):
        print ("The container usage of node %d is: " % (self.node_id))


# define controller node class
class controller:
    AP_num = 0
    C_num = 0
    profit = 0
    def __init__(self, AP_num, C_num):
        self.AP_num = AP_num
        self.C_num = C_num
    def W_allocate (self): # allocate weights of shared nodes for involved APs        
        print ("Weight reassigned. ")
    def P_collect(self): # collect profit of edge network
        
        return self.profit 

# define directed link class
class D_link:
    link_id = 0
    src_id = 0
    dst_id = 0    
    unit_cost = 1 # define the cost of carrying one unit of flow
    Avail = 1 # the availabilty of this link
    T_capacity = 100 # define the amount of traffic this link can hold
    T_load = 0 # define the amount of traffic flowing through this link
    P_delay = 0 # define the propagation delay of this link
    def __init__(self, link_id, src_id, dst_id):
        self.link_id = link_id
        self.src_id = src_id
        self.dst_id = dst_id
    def self_report(self):
        print ("I am directed link %d from %d to %d, I can hold %d traffics. " % (self.link_id, self.src_id, self.dst_id, self.T_capacity))
    def state_report(self):
        print ("The traffic usage of link %d is: " % (self.link_id))

 # define Service Function Chain request
class SFC_req:
    SFC_id = 0 # the id of this request
    SFC_len = 0 # the length of SFC measured by VNF hops
    Avail_req = 1 # minimal availabiltiy requirement 
    Bandwidth_req = 10 # minimal bandwidth requirement
    delay_req = 0 # maximal delay bound
    VNF_seq = [] # sequence of VNFs of this SFC by types
    def __init__(self, SFC_id, SFC_len):
        self.SFC_id = SFC_id
        self.SFC_len = SFC_len
    def chain_compose (self, VNF_seq): # assgin VNF type for each hop on the chain
        self.VNF_seq = VNF_seq