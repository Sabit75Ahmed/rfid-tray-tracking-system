scanned_tray = str(self.props['data'][-1]).strip()
tray_lot_map = {
    "24": "2600-002",
    "25": "2600-003",
    "26": "2600-004"
}
if scanned_tray in tray_lot_map:
    lot_number = tray_lot_map[scanned_tray]
    message = lot_number
else:
    message = "Lot Not Found: Tray " + scanned_tray

system.perspective.closePopup('View2PopUp')
system.perspective.openPopup(
    'View2PopUp', 'RFID/View2',
    params={"passedLotNumber": message},
    modal=True, overlayDismiss=True,
    position={'width': 600, 'height': 200}
)
finally:
    self.props['data'] = [self.props['data'][-1]]
