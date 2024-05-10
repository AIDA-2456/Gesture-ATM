

cfg = {
    "screen_x": 1280,
    "screen_y": 720,
    "min_detection_confidence": 0.65, # What % of confidence is required to detect the hand
    "min_tracking_confidence": 0.65, # What % of confidence is required to track the hand
    "max_num_hands": 1, # How many hands are allowed to be tracked.
    "tolerance": 0.75, # the confidence or matching % for matching two faces
    "alpha": 0.75, # The amount bleding to be done while overlaying one image on top of another
    "btnClickDelay": 1.5, # Amount of seconds the fingertips has to be inside the circle to make a click
    "btnclr" : (255, 0, 0), # BGR Colour of all the buttons
    "txtclr" : (255,255,255), # BGR Colour of all the text only on buttons
    "btnparams": {
        "W": 400, # width of the button
        "H": 80, # height of the button
        "BtnSp": 20, # space between two buttons
        "R": 40, # Radius of the button circles for each rectangle button. 1/2 * H
        "CirSp": 50 # Space between edge of rectangle and center of the circle button
    },
    "txtparams": {
        # amount of pixels by which putText origin has to be adjusted w.r.t top left corner
        # of the rectangle button
        "xadj": +20,
        "yadj": -20,
        # Integer denoting font which is HERSHEY as per CV2 module
        "font": 0,
        # Size of the font
        "fontScale": 1.8,
        # How thick the font should be
        "thickness": 2
    },
    "currentpage": "FaceRec", # Starting page is always facerec as it's the login page.
    "pages": {
        "FaceRec":{
            "pagetitle":["Select Match to match your face and Login", 100, 1.5, (255,0,0), 4],
            "buttons": ["","","","","","","","Match"],
            "navigation": ["","","","","","","","Match"]
        },
        "Transactions":{
            # List corresponding to pagetitle is as follows from left to right:
            # title text, H of text, font size, text colour, text thickness
            "pagetitle": ["Select Any Transaction", 150, 2, (255,0,0), 4],
            # Sequence of buttons wrt this list is as follows:
            # 1 -       - 2
            # 3 -       - 4
            # 5 -       - 6
            # 7 -       - 8
            "buttons":["Withdraw", "Balance", "Transfer", "Deposit", "", "" , "Exit", ""],
            # This is the "pages" to which each of these buttons will navigate to when selected.
            "navigation": ["Withdraw-SelAccType", "Balance-SelAccType", "Transfer-SelAccType",
                           "Deposit-SelAccType", "", "", "Exit", ""]
        },

        # All the pages for Withdrawal transaction
        "Withdraw-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking", "", "Credit"],
            "navigation": ["", "SelectAmountW", "", "SelectAmountW", "", "SelectAmountW"]
        },
        "SelectAmountW": {
            "pagetitle": ["Select Amount to Withdraw", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["ReceiptW","ReceiptW","ReceiptW","ReceiptW"]
        },
        "ReceiptW": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["WDDoneR", "", "WDDone"]
        },
        "WDDoneR": {
            "pagetitle": ["Please take your Card, Cash, & Receipt", 150, 1.8, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "WDDone": {
            "pagetitle": ["Please take your Card & Cash", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Balance Enquiry transaction
        "Balance-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking"],
            "navigation": ["", "ReceiptBL", "", "ReceiptBL"]
        },
        "ReceiptBL": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["BLDoneR", "", "BLDone"]
        },
        "BLDoneR": {
            "pagetitle": ["Your Balance is Rs.5000. Please take Receipt", 150, 1.5, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "BLDone": {
            "pagetitle": ["Your Balance is Rs.5000.", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Transfer transaction
        "Transfer-SelAccType" : {
            "pagetitle": ["Select Transfer Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Sav>Check", "", "Check>Sav"],
            "navigation": ["", "SelectAmountT", "", "SelectAmountT"]
        },
        "SelectAmountT": {
            "pagetitle": ["Select Amount to Transfer", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["ReceiptT","ReceiptT","ReceiptT","ReceiptT"]
        },
        "ReceiptT": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["TDoneR", "", "TDone"]
        },
        "TDoneR": {
            "pagetitle": ["Your Transfer was Successful! Please take Receipt.", 150, 1.5, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "TDone": {
            "pagetitle": ["Your Transfer was Successful!", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Deposit transaction
        "Deposit-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking"],
            "navigation": ["", "SelectAmountD", "", "SelectAmountD"]
        },
        "SelectAmountD": {
            "pagetitle": ["Select Amount to Deposit", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["Deposit","Deposit","Deposit","Deposit"]
        },
        "Deposit":{
            "pagetitle": ["Please Insert the Money", 150, 2, (255,0,0), 4],
            "buttons": ["","","","","","","","Done"],
            "navigation": ["","","","","","","","ReceiptD"]
        },
        "ReceiptD": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["DDoneR", "", "DDone"]
        },
        "DDoneR": {
            "pagetitle": ["Your Deposit was Successful! Please take Receipt.", 150, 1.5, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "DDone": {
            "pagetitle": ["Your Deposit was Successful!", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        }
    }
}
