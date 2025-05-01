$BASE_URL = "http://localhost:5000/api"

function Test-APIEndpoint {
    param (
        [string]$Endpoint,
        [string]$Method = "GET",
        [object]$Body = $null
    )

    $headers = @{
        "Content-Type" = "application/json"
    }

    $params = @{
        Uri         = "$BASE_URL/$Endpoint"  # Nota la barra después de api
        Method      = $Method
        Headers     = $headers
        ErrorAction = "Stop"
    }

    if ($Body) {
        $params["Body"] = $Body | ConvertTo-Json
    }

    try {
        $response = Invoke-RestMethod @params
        Write-Host "[SUCCESS] $Method $Endpoint" -ForegroundColor Green
        return $response
    } catch {
        Write-Host "[ERROR] $Method $Endpoint`: $($_.Exception.Message)" -ForegroundColor Red
        return $null
    }
}

# Pruebas
Write-Host "Iniciando pruebas de API..." -ForegroundColor Cyan

# 1. Crear tarea
$newTask = Test-APIEndpoint -Endpoint "tasks" -Method "POST" -Body @{
    title = "Tarea de prueba PowerShell"
    status = "pending"
}

if ($newTask) {
    $taskId = $newTask.id
    Write-Host "Tarea creada con ID: $taskId" -ForegroundColor Yellow
}

# 2. Listar tareas
Test-APIEndpoint -Endpoint "tasks" -Method "GET"

# 3. Obtener tarea específica
if ($taskId) {
    Test-APIEndpoint -Endpoint "tasks/$taskId" -Method "GET"
}

# 4. Actualizar tarea
if ($taskId) {
    Test-APIEndpoint -Endpoint "tasks/$taskId" -Method "PUT" -Body @{
        status = "completed"
    }
}

# 5. Eliminar tarea
if ($taskId) {
    Test-APIEndpoint -Endpoint "tasks/$taskId" -Method "DELETE"
}

Write-Host "Pruebas completadas" -ForegroundColor Cyan