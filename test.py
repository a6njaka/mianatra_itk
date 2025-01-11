import wx


class DraggableImage(wx.StaticBitmap):
    def __init__(self, parent, bitmap, index, on_drag_callback):
        super().__init__(parent, bitmap=bitmap)
        self.index = index
        self.on_drag_callback = on_drag_callback

        # Bind mouse events
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_MOTION, self.on_mouse_motion)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_enter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)

        # Dragging state
        self.is_dragging = False
        self.start_pos = None
        self.has_moved = False  # Tracks if the mouse was moved during dragging

        # Add black border around the image
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

    def on_left_down(self, event):
        """Handle left mouse button press."""
        self.is_dragging = True
        self.has_moved = False
        self.start_pos = event.GetPosition()
        self.CaptureMouse()
        event.Skip()

    def on_mouse_motion(self, event):
        """Handle dragging motion."""
        if self.is_dragging and event.Dragging():
            self.has_moved = True  # Mark that the mouse has moved
            # Calculate the new position
            current_pos = self.GetParent().ScreenToClient(wx.GetMousePosition())
            new_pos = (current_pos.x - self.start_pos.x, self.GetPosition().y)
            self.Move(new_pos)
        event.Skip()

    def on_left_up(self, event):
        """Handle releasing the left mouse button."""
        if self.is_dragging:
            self.is_dragging = False
            self.ReleaseMouse()
            # Only reorder if the mouse has actually moved
            if self.has_moved:
                self.on_drag_callback(self)
        event.Skip()

    def on_mouse_enter(self, event):
        """Change the cursor to a hand when over the image."""
        self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        event.Skip()

    def on_mouse_leave(self, event):
        """Reset the cursor when leaving the image."""
        self.SetCursor(wx.NullCursor)
        event.Skip()


class DraggableImageFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Draggable Images", size=(800, 400))
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        # Image file paths
        self.image_paths = [
            "images/C1.png",
            "images/C2.png",
            "images/C3.png",
            "images/C4.png",
            "images/C5.png",
        ]

        # Create a panel for displaying images
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Add images to the panel
        self.images = []
        for index, path in enumerate(self.image_paths):
            bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_PNG)
            draggable_image = DraggableImage(
                self.panel, bitmap, index, self.on_drag_end
            )
            self.images.append(draggable_image)

        # Initial layout
        self.spacing = 25  # Fixed spacing between images
        self.rebuild_layout()

    def on_drag_end(self, dragged_image):
        """Handle when an image is dropped."""
        # Find the new index based on X-position
        dragged_rect = dragged_image.GetRect()
        new_index = -1
        for i, img in enumerate(self.images):
            if dragged_image != img and dragged_rect.Intersects(img.GetRect()):
                if dragged_image.GetPosition().x < img.GetPosition().x:
                    new_index = i
                    break

        # Handle reordering
        dragged_index = self.images.index(dragged_image)
        if new_index >= 0:
            self.images.insert(new_index, self.images.pop(dragged_index))
        else:
            # If no overlap, move to the end
            self.images.append(self.images.pop(dragged_index))

        # Rebuild layout to maintain Y position and correct order
        self.rebuild_layout()

    def rebuild_layout(self):
        """Rebuild the layout to keep images in order and same Y position."""
        y_position = 50  # Fixed Y position for all images
        x_position = self.spacing  # Start X position with initial spacing

        for img in self.images:
            img.SetPosition((x_position, y_position))
            x_position += img.GetSize().GetWidth() + self.spacing

        self.panel.Refresh()  # Redraw the panel


if __name__ == "__main__":
    app = wx.App(False)
    frame = DraggableImageFrame()
    frame.Show()
    app.MainLoop()
