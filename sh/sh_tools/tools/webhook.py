from typing import List
from .base import WebhookTool, Arg
from kubiya_sdk.tools.registry import tool_registry

class WebhookTools:
    """Webhook tools for sending alerts and notifications."""

    def __init__(self):
        """Initialize and register webhook tools."""
        tools = [
            self.send_alert_webhook()
        ]
        
        for tool in tools:
            tool_registry.register("webhook", tool)

    def send_alert_webhook(self) -> WebhookTool:
        """Send an alert webhook to the specified endpoint."""
        return WebhookTool(
            name="send_alert_webhook",
            description="Send an alert webhook to notify about system events",
            content="""
            # Install required packages silently
            apk add --no-cache --quiet jq curl bash ca-certificates >/dev/null 2>&1
            
            # Define JSON payload directly with hardcoded values
            JSON_PAYLOAD='{
              "alert_id": "shiphero-queue-spike-001",
              "timestamp": "2025-04-17T13:00:00Z",
              "region": "us-east-1",
              "alert_type": "sqs_lag",
              "service_name": "order-update-worker",
              "queue_name": "OrderUpdateWebhooksQueue",
              "user_id": "client-123",
              "aws_profile": "demo",
              "log_bucket": "demo-app-logs",
              "log_prefix": "logs/order-update-worker/",
              "honeycomb_dataset": "test",
              "trace_id": "trace-abc-001"
            }'
            
            # Define the webhook URL
            WEBHOOK_URL="https://webhooksource-kubiya.hooks.kubiya.ai:8443/1lBN9HrWXW5PqiYQu3Bae0LvlVdlnk6Cvu7hsNyOsqJzm-VK_twVHYXAN9EvwyLhrPKzE1QhyzUeq5_kxCPvQNH0nOc="
            
            # Send the webhook
            echo "Sending alert webhook..."
            RESPONSE=$(curl -s -X POST "$WEBHOOK_URL" \
                -H "Content-Type: application/json" \
                -d "$JSON_PAYLOAD")
            
            # Check the response
            HTTP_STATUS=$?
            
            if [ $HTTP_STATUS -eq 0 ]; then
                echo "Webhook sent successfully!"
                echo "Response: $RESPONSE"
            else
                echo "Error sending webhook. HTTP Status: $HTTP_STATUS"
                echo "Response: $RESPONSE"
                exit 1
            fi
            """,
            args=[],  # No arguments needed as all values are hardcoded
            image="curlimages/curl:8.1.2"
        )

WebhookTools() 