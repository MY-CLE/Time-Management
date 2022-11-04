Try
{
    $WShell = New-Object -Com "Wscript.Shell"
    while (1) {
        Start-Process 'C:\windows\system32\notepad.exe'
        Start-Sleep 3
        $WShell.SendKeys("B")
        $WShell.SendKeys("i")
        $WShell.SendKeys("g")
        $WShell.SendKeys(" ")
        $WShell.SendKeys("W")
        Start-Sleep 5
        Stop-Process -Name notepad
        sleep 15 #time in sec, change to appropriate value 
    }
}
Catch
{
    Write-Host "Error"
}