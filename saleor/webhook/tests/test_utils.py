from ..event_types import WebhookEventAsyncType
from ..models import Webhook
from ..utils import get_webhooks_for_event


def test_get_webhooks_for_event(app, webhook, any_webhook, permission_manage_orders):
    app.permissions.add(permission_manage_orders)

    webhooks = get_webhooks_for_event(WebhookEventAsyncType.ORDER_CREATED)

    assert set(webhooks) == {webhook, any_webhook}


def test_get_webhooks_for_event_when_webhooks_provided(
    app, webhook, any_webhook, permission_manage_orders
):
    app.permissions.add(permission_manage_orders)

    webhooks = get_webhooks_for_event(
        WebhookEventAsyncType.ORDER_CREATED, Webhook.objects.filter(id=webhook.id)
    )

    assert webhooks.count() == 1
    assert webhooks.first() == webhook


def test_get_webhooks_for_event_when_app_has_no_permissions(app, webhook):
    webhooks = get_webhooks_for_event(WebhookEventAsyncType.ORDER_CREATED)

    assert webhooks.exists() is False


def test_get_webhook_for_event_no_duplicates(app, webhook, permission_manage_orders):
    app.permissions.add(permission_manage_orders)
    webhook.events.create(event_type=WebhookEventAsyncType.ANY)

    webhooks = get_webhooks_for_event(WebhookEventAsyncType.ORDER_CREATED)

    assert webhooks.count() == 1
