# <img src="https://cdn-icons-png.flaticon.com/512/2165/2165004.png" width="70" align="center" /> Webhook Tools for Kubiya

<div align="center">

> 🔔 Send alerts and notifications with Kubiya automation

[![Kubiya Platform](https://img.shields.io/badge/Kubiya-Platform-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAADASURBVHgBjZLBDcIwEARPCX/cAakg6YB0QEqgA6ACQgWEDkgHpAPoAFcAJUAFrGYtWbKwlGQ/Zn1n786SyZxzEfYKd4uphSunA1rX7dKAzlWQBqbB+bacc1m4wCtFg1GM4RQKLRQXeKNh4Vz/lWjBHw3X+2KmE0+oB+71M0UR1WOwHvzJ0sDgC9xh0lbOLNbk4kUBJXw8ITPU4N+rR7zQwOKXvNDgvP6GpgbOXIQRX+4ZlX4QBPbBxbpV/FV8ARfDSCg/4aaZAAAAAElFTkSuQmCC)](https://chat.kubiya.ai)
[![Webhooks](https://img.shields.io/badge/Webhooks-Powered-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://en.wikipedia.org/wiki/Webhook)
[![Docker](https://img.shields.io/badge/Docker-Powered-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

</div>

## 🎯 Overview

This module provides a webhook tool for sending alerts and notifications through Kubiya. Built on Docker containers and leveraging the power of the Kubiya platform, this tool enables seamless integration with your monitoring and alerting systems.

## 🏗️ How It Works

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#FF6C37', 'fontFamily': 'arial', 'fontSize': '16px' }}}%%
graph LR
    A([Kubiya<br/>Teammate]) -->|Trigger| B[Webhook Tool]
    B -->|POST| C[Webhook Endpoint]
    C -->|Process| D[Alert System]
    D -->|Notify| E[Response Teams]
    
    style A fill:#FF6C37,color:#fff,stroke-width:2px
    style B fill:#1a73e8,color:#fff,stroke-width:2px
    style C fill:#FF6C37,color:#fff,stroke-width:2px
    style D fill:#FF6C37,color:#fff,stroke-width:2px
    style E fill:#FF6C37,color:#fff,stroke-width:2px
```

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🚨 Alert Notifications
- Send SQS queue alerts
- Customizable alert payloads
- Timestamp and region tracking
- Service and queue identification

</td>
<td width="50%">

### 🔄 Integration
- HTTP POST requests
- JSON payload formatting
- Response handling
- Error management

</td>
</tr>
<tr>
<td width="50%">

### 📊 Monitoring
- AWS service monitoring
- Queue lag detection
- Performance tracking
- System health checks

</td>
<td width="50%">

### 🔍 Traceability
- User identification
- AWS profile tracking
- Log bucket references
- Honeycomb dataset integration

</td>
</tr>
</table>

## 📋 Prerequisites

<table>
<tr>
<td width="120" align="center">
<img src="https://cdn-icons-png.flaticon.com/512/2165/2165004.png" width="50"/>
<br/>Webhooks
</td>
<td>

- Webhook endpoint URL
- HTTP POST access
- JSON payload support
- Response handling

</td>
</tr>
<tr>
<td width="120" align="center">
<img src="https://www.docker.com/wp-content/uploads/2023/08/logo-guide-logos-1.svg" width="50"/>
<br/>Docker
</td>
<td>

- Docker runtime
- Container access
- Network connectivity
- cURL capabilities

</td>
</tr>
</table>

## 🚀 Quick Start

### 1️⃣ Install Tools

1. Visit [chat.kubiya.ai](https://chat.kubiya.ai)
2. Navigate to teammate settings
3. Install Webhook tools source
4. Configure access

### 2️⃣ Start Using

Example commands:
```
"Send alert notification"
"Trigger webhook for queue lag"
"Notify about system issue"
```

## 📚 Learn More

<table>
<tr>
<td width="33%" align="center">

[![Kubiya Docs](https://img.shields.io/badge/Kubiya-Docs-blue?style=for-the-badge&logo=readthedocs)](https://docs.kubiya.ai)

</td>
<td width="33%" align="center">

[![Webhook Info](https://img.shields.io/badge/Webhook-Info-FF6C37?style=for-the-badge&logo=postman)](https://en.wikipedia.org/wiki/Webhook)

</td>
<td width="33%" align="center">

[![Community](https://img.shields.io/badge/Join-Community-orange?style=for-the-badge&logo=slack)](https://kubiya.ai/community)

</td>
</tr>
</table>

---

<div align="center">

Built with ❤️ by the [Kubiya Community](https://chat.kubiya.ai)

<img src="https://cdn-icons-png.flaticon.com/512/2165/2165004.png" width="40" />

</div> 