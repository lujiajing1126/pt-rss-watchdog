require 'jpush'
class PushService
  cattr_reader :appkey do
    'f20d26e0f996d1668e04b57c'
  end
  cattr_reader :appsecret do
    '140b9a2cd76b445c7734c3fc'
  end
  def initialize
    @client = JPush::JPushClient.new(PushService.appkey, PushService.appsecret);
  end
  def send message
    payload = JPush::PushPayload.build(platform: JPush::Platform.all,
                                    audience: JPush::Audience.all,
                                    notification: JPush::Notification.build(alert: message)
    )
    result = @client.sendPush payload
    Rails.logger.info "Got Result #{result}"
  end
end