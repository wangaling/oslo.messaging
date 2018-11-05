# notification_listner.py
from oslo.config import cfg
import oslo_messaging
class NotificationEndpoint(object):
	filter_rule = oslo_messaging.NotificationFilter(publisher_id='^computer.*')
	def warn(self,ctxt,publisher_id,event_type,payload.metadate):
		do_something(playload)

class ErrorEndpoint(object):
	filter_rule = oslo_messaging.NotificationFilter(event_type='^instance\..*\.start$',context={'ctxt_key':'regexp'})
	def error(self,ctxt,publisher_id,event_type,payload,metadata):
		do_something(payload)
transport = oslo_messaging.get_transport(cfg.CONF)
targets = [
	oslo_messaging.Target(topic='notifications')
	oslo_messaging.Target(topic='notifications_bis')
]
endpoints = [
	NotificationEndpoint(),
	ErrorEndpoint(),
]

pool = "listener-workers"
listener = oslo_messaging.get_notification_listener(transport,targets,endpoints,pool=pool)
listener.start()
listener.wait()

